import { test } from '@playwright/test';
import { retry } from 'ts-retry';
import Log from '../../common/logger';

const suite = 'tsretry';
const log = new Log(suite);

function addTwo(x: number): number {
  log.info(`addTwo(${x})`);
  return x + 2;
}

test.describe(suite, () => {
  test('t0-addTwo', async () => {
    log.info('t0-xxx');
    const result = await retry(
      () => addTwo(7),
      {
        delay: 100,
        maxTry: 5,
        until: (lastResult: number) => (lastResult === 11)
      }
    );
    log.info(`result=${result}`);
  }); // test
}); // test.describe
