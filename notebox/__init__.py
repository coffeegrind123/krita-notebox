from krita import DockWidgetFactory, DockWidgetFactoryBase
from .notebox import NoteboxDocker

Application.addDockWidgetFactory(
    DockWidgetFactory("notebox_docker",
                     DockWidgetFactoryBase.DockRight,
                     NoteboxDocker))