import { expect, Page } from '@playwright/test';
import { retry } from 'ts-retry';
import { Utils } from './utils';
import Log from './logger';

const log = new Log('driveway');

export class Driveway {
  static async login(
    page: Page,
    workerIndex: number,
    url: string,
    email: string,
    username: string,
    password: string
  ): Promise<void> {
    const startTime = new Date().getTime();
    // precheck
    await page.goto(url);
    const url0 = 'https://www.driveway.com/';
    // Buying New & Used Cars | Driveway
    log.trace(`${workerIndex} title0: ${await page.title()} url0:${await page.url()}`);
    await expect(page.url()).toBe(url0);
    // action by entering user details and submit
    await page.getByTestId('login-btn').click();
    await page.getByTestId('email-field').click();
    await page.getByTestId('email-field').fill(email);
    await page.getByTestId('password-field').click();
    await page.getByTestId('password-field').fill(password);
    // not foolproof bec error icon becomes green even if substring is not correct
    await expect(page.getByTestId('error-icon')).not.toBeVisible();
    await page.getByTestId('login-submit-btn').click();
    // check landing page
    log.trace(`${workerIndex} title1: ${await page.title()} url1:${await page.url()}`);
    const url1 = 'https://www.driveway.com/mydriveway';
    await expect(page.url()).toBe(url1);
    // postcheck
    await expect(page.getByRole('button', { name: `Hi, ${username}` })).toBeVisible();
    const endTime = new Date().getTime();
    log.info(`${workerIndex} login ${username} ${email} - elapsed: ${endTime - startTime}`);
  }

  static async login_qe0(
    page: Page,
    workerIndex: number,
    url: string,
    email: string,
    username: string,
    password: string
  ): Promise<void> {
    const startTime = new Date().getTime();
    // precheck
    await page.goto(url);
    const url0 = 'https://www.driveway.com/';
    log.trace(`${workerIndex} title0: ${await page.title()} url0:${await page.url()}`); // Buying New & Used Cars | Driveway
    await expect(page.url()).toBe(url0);
    // action
    await page.getByTestId('login-btn').click();
    await page.getByTestId('email-field').click();
    await page.getByTestId('email-field').fill(email);
    await page.getByTestId('password-field').click();
    await page.getByTestId('password-field').fill(password);
    // not foolproof bec error icon becomes green even if substring is not correct
    await expect(page.getByTestId('error-icon')).not.toBeVisible();

    await page.getByTestId('login-submit-btn').click();
    await page.waitForLoadState('networkidle');
    log.trace(`${workerIndex} title1: ${await page.title()} url1:${await page.url()}`); // My Driveway | Driveway
    // const url1 = 'https://www.driveway.com/mydriveway';
    // const url1 = 'https://www.driveway.com/';
    // await expect(page.url()).toBe(url1);
    // postcheck
    await Utils.delay(10000);
    log.trace(`${workerIndex} title2: ${await page.title()} url2:${await page.url()}`);

    await expect(page.getByRole('button', { name: `Hi, ${username}` })).toBeVisible();
    const endTime = new Date().getTime();
    log.info(`${workerIndex} login ${username} ${email} - elapsed: ${endTime - startTime}`);
  }

  static async login_qe1(
    page: Page,
    workerIndex: number,
    url: string,
    email: string,
    username: string,
    password: string
  ): Promise<void> {
    const startTime = new Date().getTime();
    // precheck
    await page.goto(url);
    const url0 = 'https://www.driveway.com/';
    log.trace(`${workerIndex} title0: ${await page.title()} url0:${await page.url()}`); // Buying New & Used Cars | Driveway
    await expect(page.url()).toBe(url0);
    // action
    await page.getByTestId('login-btn').click();
    await page.getByTestId('email-field').click();
    await page.getByTestId('email-field').fill(email);
    await page.getByTestId('password-field').click();
    await page.getByTestId('password-field').fill(password);
    // not foolproof bec error icon becomes green even if substring is not correct
    await expect(page.getByTestId('error-icon')).not.toBeVisible();

    await page.getByTestId('login-submit-btn').click();
    // await page.waitForLoadState('networkidle');
    // ----
    let urlA = page.url();
    let countA = 1;
    while (urlA !== 'https://www.driveway.com/mydriveway' && countA < 50) {
      log.trace(`${workerIndex} ${countA} urlA:${urlA}`);
      urlA = page.url();
      await Utils.delay(500);
      countA += 1;
    }
    log.trace(`${workerIndex} ${countA} urlA:${urlA}`);
    // const url1 = 'https://www.driveway.com/mydriveway';
    // const url1 = 'https://www.driveway.com/';
    // await expect(page.url()).toBe(url1);
    // postcheck
    log.trace(`${workerIndex} title2: ${await page.title()} url2:${await page.url()}`);
    // ----
    await expect(page.getByRole('button', { name: `Hi, ${username}` })).toBeVisible();
    const endTime = new Date().getTime();
    log.info(`${workerIndex} login ${username} ${email} - elapsed: ${endTime - startTime}`);
  }

  // Temporary redirection so as to see the retries
  // Possible that ts-retry has a verbose mode but can't find it yet
  static GetPageUrl(pg: Page): string {
    const url = pg.url();
    log.trace(`GetPageUrl: ${url}`);
    return url;
  }

  static async login_qe(
    page: Page,
    workerIndex: number,
    url: string,
    email: string,
    username: string,
    password: string
  ): Promise<void> {
    const startTime = new Date().getTime();
    // precheck
    await page.goto(url);
    const url0 = 'https://www.driveway.com/';
    // Buying New & Used Cars | Driveway
    log.trace(`${workerIndex} title0: ${await page.title()} url0:${await page.url()}`);
    await expect(page.url()).toBe(url0);
    // action by entering user details and submit
    await page.getByTestId('login-btn').click();
    await page.getByTestId('email-field').click();
    await page.getByTestId('email-field').fill(email);
    await page.getByTestId('password-field').click();
    await page.getByTestId('password-field').fill(password);
    // not foolproof bec error icon becomes green even if substring is not correct
    await expect(page.getByTestId('error-icon')).not.toBeVisible();
    await page.getByTestId('login-submit-btn').click();
    // loop: make sure page.url becomes gets to landing page
    const url1 = 'https://www.driveway.com/mydriveway';
    const result = await retry(
      () => Driveway.GetPageUrl(page),
      { delay: 500, maxTry: 50, until: (lastResult: string) => lastResult === url1 }
    );
    log.trace(`${workerIndex} result=${result}`);
    await expect(page.url()).toBe(url1);
    // postcheck
    await expect(page.getByRole('button', { name: `Hi, ${username}` })).toBeVisible();
    const endTime = new Date().getTime();
    log.info(`${workerIndex} login ${username} ${email} - elapsed: ${endTime - startTime}`);
  }

  static async logout(
    page: Page,
    workerIndex: number,
    username: string
  ): Promise<void> {
    const startTime = new Date().getTime();
    // missing precheck
    // action
    await page.getByRole('button', { name: `Hi, ${username}` }).click();
    await page.getByRole('menuitem', { name: 'Log Out' }).click();
    await expect(page).toHaveTitle(/Driveway/);
    // missing postcheck
    const endTime = new Date().getTime();
    log.info(`${workerIndex} logout - elapsed: ${endTime - startTime}`);
  }
} // class Driveway

export default Driveway;
