/* eslint-disable @typescript-eslint/no-unused-vars */
import { expect, Page } from '@playwright/test';
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
    // precheck?
    // action
    await page.goto(url);
    await page.getByTestId('login-btn').click();
    await page.getByTestId('email-field').click();
    await page.getByTestId('email-field').fill(email);
    await page.getByTestId('password-field').click();
    await page.getByTestId('password-field').fill(password);
    await page.getByTestId('login-submit-btn').click();
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
    // missing postcheck
    const endTime = new Date().getTime();
    log.info(`${workerIndex} logout - elapsed: ${endTime - startTime}`);
  }
} // class Driveway

export default Driveway;
