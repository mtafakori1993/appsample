// Captures local HTML screens into Figma as editable layers using Figma's capture script.
// usage: node figma_capture.cjs <playwright-core path> <chromium exe> <jobs.json> <capture.js path>
// Honors HTTPS_PROXY from the environment (needed on networks that route outbound traffic through a proxy).
const [,, pwPath, exe, jobsFile, captureJs] = process.argv;
const { chromium } = require(pwPath);
const jobs = JSON.parse(require('fs').readFileSync(jobsFile, 'utf8'));
(async () => {
  const browser = await chromium.launch({ executablePath: exe, headless: true, ...(process.env.HTTPS_PROXY ? { proxy: { server: process.env.HTTPS_PROXY.replace(/\/$/, ''), bypass: 'localhost,127.0.0.1' } } : {}) });
  for (const j of jobs) {
    const ctx = await browser.newContext({ viewport: { width: 1600, height: 1200 } });
    const page = await ctx.newPage();
    try {
      await page.goto(j.url, { waitUntil: 'networkidle' });
      await page.addStyleTag({ content: '.bezel{zoom:1 !important}' });
      const src = require('fs').readFileSync(captureJs, 'utf8');
      await page.evaluate((s) => { const el = document.createElement('script'); el.textContent = s; document.head.appendChild(el); }, src);
      await page.waitForTimeout(800);
      // The capture promise may stay pending after the upload completes, so fire it and wait a fixed interval.
      page.evaluate(({ id, sel }) => window.figma.captureForDesign({ captureId: id, endpoint: `https://mcp.figma.com/mcp/capture/${id}/submit?bindVariables=true`, selector: sel }), { id: j.captureId, sel: j.selector }).catch(() => {});
      await page.waitForTimeout(j.wait || 25000);
      console.log('SUBMITTED', j.name);
    } catch (e) { console.log('FAIL', j.name, String(e).slice(0, 200)); }
    await ctx.close();
  }
  await browser.close();
})();
