/** announce.spec.ts
  Unit tests for common.announce.ts
  Announce function is (im)purely used for its side effects, ie printing to console
  Hence, no verification or expect statements
  Just run and view
*/
import { test } from '@playwright/test';
import { Announce } from '../../common/announce';

const suiteName = 'announce-unittests';

test.describe(suiteName, () => {
  test('t1-announce', async ({ browser }, workerInfo) => {
    // No need to log since announce will do so
    // This test will always pass since I am relying on a visual check
    Announce.announce(browser, workerInfo.workerIndex);
  });
});
