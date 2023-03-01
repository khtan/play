(ert-deftest t0-fill-column-is-a-variable()
  (should
    (string-equal
      "fill-column: 70"
      (message "fill-column: %d" fill-column)
    )
  )
)
(ert-deftest t1-fill-column-is-not-a-function()
  :expected-result :failed
  (fill-column)
)
