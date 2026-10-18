from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.graphics import Color, RoundedRectangle
from kivy.utils import get_color_from_hex
import datetime
import calendar

class ModernCard(BoxLayout):
    def __init__(self, bg_hex="#1E293B", radius=12, **kwargs):
        super().__init__(**kwargs)
        self.padding = 15
        self.spacing = 10
        with self.canvas.before:
            Color(*get_color_from_hex(bg_hex))
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[radius])
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

class UtilityApp(App):
    def build(self):
        tp = TabbedPanel(do_default_tab=False, tab_width=100, background_color=get_color_from_hex("#0F172A"))

        # 1. Clock Tab
        clock_tab = TabbedPanelHeader(text='Clock', background_color=get_color_from_hex("#6366F1"))
        clock_layout = BoxLayout(orientation='vertical', padding=20)
        clock_card = ModernCard(bg_hex="#1E293B", orientation='vertical')
        self.time_label = Label(text="00:00:00", font_size='36sp', bold=True, color=get_color_from_hex("#38BDF8"))
        self.date_label = Label(text="Loading...", font_size='16sp', color=get_color_from_hex("#94A3B8"))
        clock_card.add_widget(self.time_label)
        clock_card.add_widget(self.date_label)
        clock_layout.add_widget(clock_card)
        Clock.schedule_interval(self.update_clock, 1)
        clock_tab.content = clock_layout
        tp.add_widget(clock_tab)

        # 2. Browser Tab
        browser_tab = TabbedPanelHeader(text='Browser', background_color=get_color_from_hex("#0D9488"))
        browser_layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        search_card = ModernCard(bg_hex="#1E293B", size_hint_y=0.2)
        url_input = TextInput(text='https://www.google.com', multiline=False, background_color=get_color_from_hex("#334155"), foreground_color=get_color_from_hex("#FFFFFF"), padding=[10, 10, 10, 10])
        btn_go = Button(text='Go', size_hint_x=0.3, background_color=get_color_from_hex("#14B8A6"), background_normal='')
        search_card.add_widget(url_input)
        search_card.add_widget(btn_go)
        browser_layout.add_widget(search_card)
        browser_tab.content = browser_layout
        tp.add_widget(browser_tab)

        # 3. Compass Tab
        compass_tab = TabbedPanelHeader(text='Compass', background_color=get_color_from_hex("#EA580C"))
        compass_layout = BoxLayout(orientation='vertical', padding=20)
        compass_card = ModernCard(bg_hex="#1E293B", orientation='vertical')
        compass_card.add_widget(Label(text="Compass Direction", font_size='18sp', color=get_color_from_hex("#FDBA74")))
        compass_card.add_widget(Label(text="0° North", font_size='32sp', bold=True, color=get_color_from_hex("#FB923C")))
        compass_layout.add_widget(compass_card)
        compass_tab.content = compass_layout
        tp.add_widget(compass_tab)

        # 4. Calendar Tab
        cal_tab = TabbedPanelHeader(text='Calendar', background_color=get_color_from_hex("#8B5CF6"))
        cal_layout = BoxLayout(orientation='vertical', padding=20)
        cal_card = ModernCard(bg_hex="#1E293B", orientation='vertical')
        now = datetime.datetime.now()
        cal_card.add_widget(Label(text=calendar.month(now.year, now.month), font_size='14sp', color=get_color_from_hex("#C084FC")))
        cal_layout.add_widget(cal_card)
        cal_tab.content = cal_layout
        tp.add_widget(cal_tab)

        return tp

    def update_clock(self, dt):
        now = datetime.datetime.now()
        self.time_label.text = now.strftime('%I:%M:%S %p')
        self.date_label.text = now.strftime('%A, %B %d, %Y')

if __name__ == '__main__':
    UtilityApp().run()
