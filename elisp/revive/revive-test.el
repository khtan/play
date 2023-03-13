;; The invocation has interaction with the shell
;;  | kwee1-ubuntu | emacs shell works
;;  | air          | emacs shell does not work
;;  | air          | git bash shell works
;;    emacs -batch -l ert -l revive1-outshine.el -l revive-test.el -eval '(ert-run-tests-batch-and-exit "t0")'

(require 'ert)
;; t0-hello-world
(ert-deftest t0-hello-world()
  (let ((msg "t0-hello-world"))
    (message "msg: %s" msg)
  )
)
;; t1
(ert-deftest t1-configuration-file()
  (let ((msg "t1-configuration-file"))
    (message "revive:configuration-file: %s" revive:configuration-file)
  )
)

