import sys
from waflib.extras.preparation import PreparationContext
from waflib.extras.filesystem_utils import removeSubdir

def options(optCtx):
    optCtx.load('dep_resolver')

def prepare(prepCtx):
    prepCtx.options.dep_base_dir = prepCtx.srcnode.find_dir('..').abspath()
    prepCtx.load('dep_resolver')
    removeSubdir(prepCtx.path.abspath(), 'lib', 'include', 'share')
    if sys.platform == 'linux2':
	prepCtx.recurse('libunwind')
    prepCtx.recurse('glog')

def configure(confCtx):
    confCtx.load('dep_resolver')
    confCtx.recurse('glog')

def build(buildCtx):
    buildCtx.recurse('glog')
