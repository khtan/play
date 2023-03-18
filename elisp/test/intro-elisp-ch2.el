;; * comments
;;    emacs -batch -l ert -l intro-elisp-ch2.el -eval '(ert-run-tests-batch-and-exit "t2-1")'
;; * tests
(require 'ert)
;; ** useful functions
(defun print-buffer-info (bname)
  "Prints information about a buffer"
  (with-current-buffer bname
    (message "buffer-name: %s" (buffer-name))
    (message "buffer-file-name: %s" (buffer-file-name))
    (message "buffer-size: %s" (buffer-size))
    (message "buffer min, point, max : %d %d %d" (point-min) (point) (point-max))
    (message "nondirectory: %s" (file-name-nondirectory buffer-file-name))
  )
)
(defun create-buffer (fpath)
  "Creates a buffer from fpath"
  (buffer (find-file-noselect filename))
)
;; ** preliminary files and paths
(ert-deftest t0-useful-functions()
  "?"
  (let
    ((filepath "~/projects/github/play/elisp/test/intro-elisp-ch2.el"))
    (message "filepath: %s" filepath)
    (message "file-name-nondirectory: %s" (file-name-nondirectory filepath))
    (message "file-name-base: %s" (file-name-base filepath))
    (message "file-name-extension: %s" (file-name-extension filepath))
  );; let
);; ert

;; ** 2.1 buffer names
(ert-deftest t2-1-buffer-name()
  "?"
  (let ((filename "~/projects/github/play/elisp/test/intro-elisp-ch2.el"))
    (with-temp-buffer
      (insert-file-contents filename)
      ;; (message "buffer-name: %s" buffer-name)
      ;; (message "buffer-file-name: %s" buffer-file-name)
      (should (equal (buffer-file-name) filename))
    )
  )
)

(ert-deftest test-buffer-file-name ()
  "Test that buffer-file-name is correct after loading a file."
  (let ((filename "/home/tankh/projects/github/play/elisp/test/intro-elisp-ch2.el"))
    (with-temp-buffer
      (insert-file-contents filename)
      (should (equal (buffer-file-name) filename)))))

(ert-deftest test2-buffer-file-name ()
  "Test that buffer-file-name is correct after loading a file."
  (let* ((filename "/home/tankh/projects/github/play/elisp/test/intro-elisp-ch2.el")
         (buffer (find-file-noselect filename)))
    (unwind-protect
        (with-current-buffer buffer
          (should (equal (buffer-file-name) filename)))
      (kill-buffer buffer))))

(ert-deftest test3-buffer-file-name ()
  "Test that buffer-file-name is correct after loading a file."
  (let* ((filename "intro-elisp-ch2.el")
         (buffer (find-file-noselect filename)))
    (unwind-protect
      (with-current-buffer buffer
        (should (equal (file-name-nondirectory buffer-file-name) filename))
        (should (equal (buffer-name) filename))
      )
      (kill-buffer buffer)
    )
  )
)
(ert-deftest t2-x ()
  "?"
  (let* ((filename "intro-elisp-ch2.el")
         (buffer (find-file-noselect filename)))
    (unwind-protect
      (with-current-buffer buffer
        (print-buffer-info buffer)
        (should (equal (buffer-name) filename))
        (should (equal (file-name-nondirectory buffer-file-name) filename))
        (should (equal buffer-file-name (expand-file-name filename)))
        (should (equal (buffer-file-name) (expand-file-name filename)))
      )
    )
    (kill-buffer buffer)
  )
)
(ert-deftest t2-scratch-buffer ()
  "Test the buffer-name and buffer-file-name of the scratch buffer."
  (with-current-buffer (get-buffer-create "*scratch*")
    (should (equal (buffer-name) "*scratch*"))
    (should (equal (buffer-file-name) nil))))
(ert-deftest t2-scratch-buffer-contents ()
  "Test the contents of the scratch buffer."
  (with-current-buffer (switch-to-buffer "*scratch*")
    (should (equal (buffer-name) "*scratch*"))
    (should (equal (buffer-file-name) nil))
    (insert "Some content in the scratch buffer\n")
    (should (equal (buffer-string) "Some content in the scratch buffer\n"))))
(ert-deftest test-scratch-buffer-contents ()
  "Test the contents of the scratch buffer."
  (with-current-buffer (current-buffer)
    (should (equal (buffer-name) "*scratch*"))
    (should (equal (buffer-file-name) nil))
    (insert "Some content in the scratch buffer\n")
    (should (equal (buffer-string) "Some content in the scratch buffer\n"))))
(ert-deftest test2-scratch-buffer-contents ()
  "Test the contents of the scratch buffer."
  (let ((old-buffer (current-buffer)))
    (switch-to-buffer "*scratch*")
    (should (equal (buffer-name) "*scratch*"))
    (should (equal (buffer-file-name) nil))
    (insert "Some content in the scratch buffer\n")
    (should (equal (buffer-string) "Some content in the scratch buffer\n"))
    (switch-to-buffer old-buffer)))

