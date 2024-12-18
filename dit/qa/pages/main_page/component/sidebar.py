from coms.qa.frontend.pages.component import Component, ComponentWrapper

__all__ = ['Sidebar']


class SidebarWrapper(ComponentWrapper):
    recently = Component(id="recentlyViewedSidebar")
    favorite = Component(id="favoritesSidebar")

    @property
    def is_visible(self) -> bool:
        assert self.recently.visible

        return self.favorite.visible


class Sidebar(Component):
    def __get__(self, instance, owner) -> SidebarWrapper:
        return SidebarWrapper(instance.app, self.find(instance), self._locator)
