from import_shims.warn import warn_deprecated_import

warn_deprecated_import('instructor_task.tests.test_tasks', 'lms.djangoapps.instructor_task.tests.test_tasks')

from lms.djangoapps.instructor_task.tests.test_tasks import *
