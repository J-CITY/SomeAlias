from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu, RightContent
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import RectangularElevationBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty
import random

KV = """
<RightContentCls>
    disabled: True

    MDIconButton:
        icon: root.icon
        user_font_size: "16sp"
        pos_hint: {"center_y": .5}

    MDLabel:
        text: root.text
        font_style: "Caption"
        size_hint_x: None
        width: self.texture_size[0]
        text_size: None, None


<CustomToolbar>:
    size_hint_y: None
    height: self.theme_cls.standard_increment
    padding: "5dp"
    spacing: "12dp"

    MDIconButton:
        id: button_1
        icon: "menu"
        pos_hint: {"center_y": .5}
        on_release: app.menu_1.open()

    MDLabel:
        text: "SomeAlias"
        pos_hint: {"center_y": .5}
        size_hint_x: None
        width: self.texture_size[0]
        text_size: None, None
        font_style: 'H6'


Screen:

    CustomToolbar:
        id: toolbar
        elevation: 10
        pos_hint: {"top": 1}
    BoxLayout:
        size_hint: None, None
        width: self.minimum_width
        height: dp(56)
        orientation: "vertical"
        spacing: "50dp"
        pos_hint: {"center_x": .5, "center_y": .5}

        MDLabel:
            id: countId
            text: app.countStr
            valign: "top"
            halign: "center"
            font_style: "H3"

        MDCard:
            size_hint: None, None
            size: "280dp", "180dp"
            pos_hint: {"center_x": .5, "center_y": .5}
            MDLabel:
                id: wordId
                text: app.curWord
                halign: "center"
                font_style: "H4"


    FloatLayout:
        MDFloatingActionButton:
            icon: "check"
            pos_hint: {'center_x': .8, 'center_y': .1}
            on_release: app.onOk()
            md_bg_color: 0.1953125, 0.65625, 0.3203125, 1
        MDFloatingActionButton:
            icon: "close"
            pos_hint: {'center_x': .2, 'center_y': .1}
            on_release: app.onCancle()
            md_bg_color: 0.65625, 0.1953125, 0.1953125, 1
"""

hardPack = [
    "улучшение",
    "аллергик",
    "приветствие",
    "водворение",
    "минералогия",
    "перепел",
    "угодник",
    "нумерация",
    "мироздание",
    "эфир",
    "водопровод",
    "лазурь",
    "одухотворение",
    "отбор",
    "языкознание",
    "звукоприёмник",
    "письменность",
    "утверждение",
    "показатель",
    "посланник",
    "противоядие",
    "темперамент",
    "каподастр",
    "отговорка",
    "эгоцентричность",
    "хранилище",
    "крохоборство",
    "горилла",
    "аналитик",
    "разница",
    "репертуар",
    "бездумье",
    "пеликан",
    "достояние",
    "сват",
    "агрегат",
    "кукан",
    "байка",
    "литавры",
    "заступник",
    "подстрекатель",
    "петиция",
    "мореплавание",
    "агентство",
    "самоуничтожение",
    "протон",
    "шурин",
    "правосудие",
    "искусствовед",
    "смерд",
    "натура",
    "фазенда",
    "социология",
    "конфуз",
    "утварь",
    "грымза",
    "бронемашина",
    "нервотрепка",
    "гарь",
    "гуляка",
    "великомученик",
    "аллигатор",
    "сталагмит",
    "наследие",
    "птицеводство",
    "расценка",
    "ратуша",
    "крестьянин",
    "притаптывание",
    "уплата",
    "радиосвязь",
    "анфас",
    "гениальность",
    "фантасмагория",
    "республиканец",
    "яйцерезка",
    "стычка",
    "отплытие",
    "скопление",
    "рецептура",
    "кобель",
    "зимовье",
    "вынашивание",
    "твердыня",
    "котлован",
    "правдоискатель",
    "застенок",
    "номенклатура",
    "пасынок",
    "кляссер",
    "высокомерие",
    "паводок",
    "личина",
    "доломит",
    "филистер",
    "эдикт",
    "аракчеевщина",
    "абсорбция",
    "антагонизм",
    "каландр",
    "амбивалентность",
    "трудотерапия",
    "тяжелодум",
    "горемыка",
    "идентификация",
    "камердинер",
    "ямс",
    "танцмейстер",
    "варьете",
    "культиватор",
    "униформист",
    "евнух",
    "аардоникс",
    "ошеломление",
    "ординарец",
    "конструктивист",
    "водевиль",
    "горовосходитель",
    "шрапнель",
    "опылитель",
    "глаголица",
    "животновод",
    "летосчисление",
    "мезонин",
    "канонир",
    "метизы",
    "банджо",
    "патронесса",
    "разнотолки",
    "эпителий",
    "нейтралитет",
    "зипун",
    "колчан",
    "подхалим",
    "кандибобер",
    "общность",
    "фарцовщик",
    "молибден",
    "кабала",
    "расстегай",
    "тепидарий",
    "субстантивация",
    "бахвал",
    "обормот",
    "сейсмограф",
    "военщина",
    "ванилин",
    "гидропоника",
    "конвенция",
    "либерализм",
    "магистраль",
    "опреснитель",
    "лигатура",
    "сомнамбулизм",
    "синопсис",
    "упадочничество",
    "болтология",
    "супостат",
    "колониализм",
    "борона",
    "чинопочитание",
    "самообольщение",
    "шерстопрядение",
    "топчан",
    "эндокринология",
    "востоковед",
    "астеризм",
    "огнепоклонничество"
]


class RightContentCls(RightContent):
    pass


class CustomToolbar(ThemableBehavior, RectangularElevationBehavior, MDBoxLayout,):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = self.theme_cls.primary_color


class Test(MDApp):
    count = 0
    countStr = StringProperty()
    wordId = 0
    curWord = StringProperty()
    words = hardPack

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        self.menu_1 = self.create_menu(
            "Replay", self.screen.ids.toolbar.ids.button_1
        )

        self.restart()

    def restart(self):
        self.count = 0
        self.wordId = 0
        random.shuffle(self.words)
        self.curWord = self.words[0]
        self.countStr = "0"

    def create_menu(self, text, instance):
        menu_items = [
            {
                "right_content_cls": RightContentCls(
                    text="", icon="",
                ),
                "icon": "replay",
                "text": text
            }
        ]
        return MDDropdownMenu(caller=instance, items=menu_items, width_mult=5,
            callback=self.menuCallback)

    def build(self):
        return self.screen

    def onOk(self):
        self.count += 1
        self.countStr = str(self.count)
        self.wordId = (self.wordId+1) % len(self.words)
        self.curWord = self.words[self.wordId]
    
    def onCancle(self):
        self.wordId = (self.wordId+1) % len(self.words)
        self.curWord = self.words[self.wordId]
    def menuCallback(self, instance):
        self.restart()
Test().run()