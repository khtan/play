import { configure, getLogger, Logger } from 'log4js';

/**
 * This is intended to keep logging functions in one class
 */
export default class Log {
  private static instance: Log;

  private logger: Logger;

  constructor(name: string) {
    configure({
      appenders: { console: { type: 'console' } },
      categories: { default: { appenders: ['console'], level: 'debug' } }
    });
    // ToDo: This is a limitation by naming the singleton logger as 'E2E'
    // It means that all test output through logging will have module E2E,
    // which does not provide useful information
    // Far better to allow loggers to be more fine-grained.
    this.logger = getLogger(name);
  }

  public static getInstance(): Log {
    if (!Log.instance) {
      Log.instance = new Log('E2E');
    }

    return Log.instance;
  }

  public fatal(message: string): void { this.logger.fatal(message); }

  public error(message: string): void { this.logger.error(message); }

  public warn(message: string): void { this.logger.warn(message); }

  public info(message: string): void { this.logger.info(message); }

  public debug(message: string): void { this.logger.debug(message); }

  public trace(message: string): void { this.logger.trace(message); }
}
