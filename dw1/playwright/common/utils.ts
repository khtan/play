import Log from './logger';

export class Utils {
  private static log: Log = new Log('utils');

  static async delay(time: number) {
    return new Promise((resolve) => {
      setTimeout(resolve, time);
    });
  }
} // class Utils

export default Utils;
