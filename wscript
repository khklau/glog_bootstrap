import os
import sys
from waflib.extras.build_status import BuildStatus
from waflib.extras.preparation import PreparationContext
from waflib.extras.filesystem_utils import removeSubdir

def options(optCtx):
    optCtx.load('dep_resolver')

def prepare(prepCtx):
    prepCtx.options.dep_base_dir = prepCtx.srcnode.find_dir('..').abspath()
    prepCtx.load('dep_resolver')
    if sys.platform == 'linux2':
	try:
	    lstatus = BuildStatus.load(os.path.join(prepCtx.path.abspath(), 'libunwind'))
	    if not lstatus.isSuccess():
		removeSubdir(prepCtx.path.abspath(), 'lib', 'include', 'share')
	except ValueError:
	    removeSubdir(prepCtx.path.abspath(), 'lib', 'include', 'share')
	finally:
	    prepCtx.recurse('libunwind')
	    prepCtx.recurse('glog')
    else:
	try:
	    gstatus = BuildStatus.init(os.path.join(prepCtx.path.abspath(), 'glog'))
	    if not gstatus.isSuccess():
		removeSubdir(prepCtx.path.abspath(), 'lib', 'include', 'share')
	except ValueError:
	    removeSubdir(prepCtx.path.abspath(), 'lib', 'include', 'share')
	finally:
	    prepCtx.recurse('glog')

def configure(confCtx):
    confCtx.load('dep_resolver')
    confCtx.recurse('glog')

def build(buildCtx):
    buildCtx.recurse('glog')
