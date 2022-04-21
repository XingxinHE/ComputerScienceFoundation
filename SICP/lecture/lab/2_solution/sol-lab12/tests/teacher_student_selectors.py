test = {
  'name': 'teacher_student_selectors',
  'points': 1,
  'suites': [
    {
      'type': 'scheme',
      'setup': r"""
      scm> (load-all ".")
      """,
      'cases': [
        {
          'code': r"""
          scm> (define student-john (student-create 'john '(astronomy))) ; a student named John who has attended astronomy once
          student-john
          scm> (student-get-name student-john)
          john
          scm> (student-get-classes student-john)
          (astronomy)
          scm> (define student-jamie (student-create 'jamie '(astronomy astronomy))) ; a student named Jamie who has attended astronomy twice
          student-jamie
          scm> (student-get-name student-jamie)
          jamie
          scm> (student-get-classes student-jamie)
          (astronomy astronomy)
          scm> (define students (cons student-john (cons student-jamie nil)))
          students
          scm> (define teacher-pamela (teacher-create 'pamela 'cs61a students)) ; they are pamela's students!
          teacher-pamela
          scm> (teacher-get-name teacher-pamela)
          pamela
          scm> (teacher-get-class teacher-pamela)
          cs61a
          scm> (map student-get-name (teacher-get-students teacher-pamela))
          (john jamie)
          scm> (map student-get-classes (teacher-get-students teacher-pamela))
          ((astronomy) (astronomy astronomy))
          """,
          "locked": False
        },
      ],
    },
  ]
}