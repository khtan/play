/* eslint-disable @typescript-eslint/no-unused-vars */
import { expect, Page } from '@playwright/test';
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
    const url1 = 'https://www.driveway.com/mydriveway';
    await expect(page.url()).toBe(url1);
    // postcheck
    await expect(page.getByRole('button', { name: `Hi, ${username}` })).toBeVisible();
    const endTime = new Date().getTime();
    log.info(`${workerIndex} login ${username} ${email} - elapsed: ${endTime - startTime}`);
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
    const url1 = 'https://www.driveway.com/';
    // await expect(page.url()).toBe(url1);
    // postcheck
    await Utils.delay(10000);
    log.trace(`${workerIndex} title2: ${await page.title()} url2:${await page.url()}`); 

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
