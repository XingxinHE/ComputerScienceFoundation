test = {
  'name': 'interleave',
  'points': 1,
  'suites': [
    {
      'scored': True,
      'setup': """
      scm> (load-all ".")
      """,
      'type': 'scheme',
      'cases': [
        {
          'code': """
          scm> (interleave (list 1 3 5) (list 2 4))
          (1 2 3 4 5)
          """,
          'hidden': False
        },
        {
          'code': """
          scm> (interleave (list 2 4) (list 1 3 5))
          (2 1 4 3 5)
          """,
          'hidden': False
        },
        {
          'code': """
          scm> (interleave (list 1 2) (list 1 2))
          (1 1 2 2)
          """,
          'hidden': False
        },
        {
          'code': """
          scm> (interleave '(1 2 3 4 5 6) '(7 8))
          (1 7 2 8 3 4 5 6)
          """,
          'hidden': False
        },
      ]
    },
    {
      'scored': True,
      'setup': """
      scm> (load-all ".")
      """,
      'type': 'scheme',
      'cases': [
        {
          'code': """
          scm> (interleave (list 1 3 5) (list 2 4 6))
          (1 2 3 4 5 6)
          """,
          'hidden': False
        },
        {
          'code': """
          scm> (interleave (list 1 3 5) nil)
          (1 3 5)
          scm> (interleave nil (list 1 3 5))
          (1 3 5)
          scm> (interleave nil nil)
          ()
          """,
          'hidden': False
        },
      ]
    }
  ]
}