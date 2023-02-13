(require 'ert)
(ert-deftest t0-hello-world()
  (let ((msg "hello world"))
    (should (equal msg "hello xworld"))
    (message msg)
  )
)
(ert-deftest t1-list-of-flowers()
  (let ((flowers `(rose violet daisy buttercup)))
    (message "flowers: %s" flowers)
    ))
