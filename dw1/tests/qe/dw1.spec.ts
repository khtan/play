import { test, expect } from '@playwright/test';
import Log from '../../common/logger';

const log = new Log('dw1');

test.describe('', () => {
  test('t0-has-title', async ({ browserName, page }, testInfo) => {
    await page.goto('http://driveway.com');

    // Expect a title "to contain" a substring.
    const title = await page.title();
    log.info(`${testInfo.workerIndex} ${browserName} ${testInfo.title}: page.title= ${title}`);
    await expect(page).toHaveTitle(/Driveway/);
  });
}); // describe
