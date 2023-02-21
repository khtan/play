/** announce.ts
    This library logs all the external dependencies like OS and Playwright version.
    This is useful when looking at logs and for debugging.
    nogui/announce.spec.ts is a simple unit test
    Currently using the side effect of log.info
    If necessary, can create a data structure and then print out the structure,
    but this is simplest for now.
*/
import os from 'os';
import { Browser } from '@playwright/test';
import Log from './logger';

const pwVersion = require('@playwright/test/package.json').version;

export class Announce {
  private static log: Log = new Log('announce');

  public static printPlaywrightVersion(workerIndex: number) {
    Announce.log.info(`${workerIndex} playwright:\t${pwVersion}`);
  }

  public static printOS(workerIndex: number) {
    Announce.log.info(`${workerIndex} hostname:\t${os.hostname()}`);
    Announce.log.info(`${workerIndex} os type:\t${os.type()}`);
    Announce.log.info(`${workerIndex} platform:\t${os.platform()}`);
    Announce.log.info(`${workerIndex} arch:\t${os.arch()}`);
    Announce.log.info(`${workerIndex} num cpus:\t${os.cpus().length}`);
    Announce.log.info(`${workerIndex} freemem:\t${os.freemem()}`);
    Announce.log.info(`${workerIndex} totalmem:\t${os.totalmem()}`);
  }

  public static printBrowser(browser: Browser, workerIndex: number) {
    Announce.log.info(`${workerIndex} browser:\t${browser.browserType().name()} ${browser.version()}`);
  }

  public static printEnv(workerIndex: number) {
    // environment USER for Linux, USERNAME for Windows, not set for TeamCity
    const userName = process.env.USER || process.env.USERNAME || 'not set';
    Announce.log.info(`${workerIndex} user:\t${userName}`);
  }

  /** This is intended to be the convenient entry point to announce everything
  */
  public static announce(browser: Browser, workerIndex: number = -1) {
    Announce.printPlaywrightVersion(workerIndex);
    Announce.printOS(workerIndex);
    Announce.printBrowser(browser, workerIndex);
    Announce.printEnv(workerIndex);
  }
}

export default Announce;
