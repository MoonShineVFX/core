"""Public API

Anything that isn't defined here is INTERNAL and unreliable for external use.

"""
import pipeline
from .pipeline import (
    install,
    uninstall,
    Creator,
    Loader,

    ls,
    load,
    create,
    update,
    remove,
    publish,
    containerise
)

#     update,
#     publish,
#     containerise,
# 
#     lock,
#     unlock,
#     is_locked,
#     lock_ignored,


from .lib import (
#     export_alembic,
#     lsattr,
#     lsattrs,
#     read,
#
#     apply_shaders,
#     without_extension,
    maintained_selection,
#     suspended_refresh,
#
#     unique_name,
#     unique_namespace,
)

from .workio import (
    open_file,
    save_file,
    current_file,
    has_unsaved_changes,
    file_extensions,
    work_root
)

__all__ = [
    "install",
    "uninstall",

    "Creator",
    "Loader",

    "ls",
    "load",
    "create",
    "remove",

#     "update",
#     "read",
    "publish",
# 
#     "lock",
#     "unlock",
#     "is_locked",
#     "lock_ignored",

    #     "export_alembic",
    #     "lsattr",
    #     "lsattrs",
    #
    #     "unique_name",
    #     "unique_namespace",
    #
    #     "apply_shaders",
    #     "without_extension",
        "maintained_selection"]
    #     "suspended_refresh",
    #
    #     "containerise",

