;; The invocation has interaction with the shell
;;  | kwee1-ubuntu | emacs shell works
;;  | air          | emacs shell does not work
;;  | air          | git bash shell works
;;    emacs -batch -l ert -l revive1-outshine.el -l revive-test.el -eval '(ert-run-tests-batch-and-exit "t0")'

(require 'ert)
;; * tests
;; ** intro tests
;; i0-hello-world
(ert-deftest i0-hello-world()
  (let ((msg "i0-hello-world"))
    (message "msg: %s" msg)
  )
)
;; i1
(ert-deftest i1-configuration-file()
  (let ((msg "i1-configuration-file"))
    (message "revive:configuration-file: %s" revive:configuration-file)
  )
)
;; i2
(ert-deftest i2-global-variable()
  (let ((msg "i2"))
    (message "truncate-partial-width-windows: %s" truncate-partial-width-windows)
    (message "make-backup-files: %s" make-backup-files)
    (message "version-control: %s" version-control)
    (message "visible-bell: %s" visible-bell)
    (message "file-name-history: %s" file-name-history)
    (message "buffer-name-history: %s" buffer-name-history)
    (message "minibuffer-history: %s" minibuffer-history)
  )
)
(defun check-file-exists (desc file-path)
  "Check if a file exists at FILE-PATH and print a message indicating whether it does or not."
  (if (file-exists-p file-path)
      (message "%s file exists at %s" desc file-path)
    (message "%s file does not exist at %s" desc file-path)))
;; ** revive tests
(ert-deftest t1-save-current-configuration()
  (let ((msg "t1-xxx"))
    (message "revive:configuration-file: %s" revive:configuration-file)
    (check-file-exists "before" revive:configuration-file)
    (save-current-configuration)
    (check-file-exists "after" revive:configuration-file)
  )
)

