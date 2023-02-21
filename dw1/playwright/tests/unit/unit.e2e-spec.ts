import { test } from '@playwright/test';
import { Driveway as Dw } from '../../common/driveway';
import { Announce } from '../../common/announce';

test.describe('unittests', () => {
  test.beforeAll(async ({browser}, testInfo) =>{
    Announce.announce(browser, testInfo.workerIndex);
  });
  test('t0-unitloginlogout', async ({ page }, testInfo) => {
    await Dw.login_qe(page, testInfo.workerIndex, 'http://www.driveway.com', 'tan.k.h.usa@gmail.com', 'Kwee', 'JalanMasuk4!');
    await Dw.logout(page, testInfo.workerIndex, 'Kwee');
    console.log('end of test');
  }); // test
}); // describe
