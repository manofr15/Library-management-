import json
import os

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window


# -------------------------------------------------
# WINDOW / BACKGROUND
# -------------------------------------------------

Window.clearcolor = (0.94, 0.97, 1, 1)

DATA_FILE = "library.json"


# -------------------------------------------------
# DATABASE FUNCTIONS
# -------------------------------------------------

def load_books():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except:
            return []
    return []


def save_books():
    with open(DATA_FILE, "w") as f:
        json.dump(library, f, indent=4)


library = load_books()


# -------------------------------------------------
# MAIN APPLICATION
# -------------------------------------------------

class LibraryApp(App):

    def build(self):

        # Main layout
        self.root_layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=12
        )

        # -------------------------------------------------
        # TITLE
        # -------------------------------------------------

        self.title_label = Label(
            text="LIBRARY MANAGER",
            font_size=28,
            bold=True,
            color=(0.05, 0.20, 0.60, 1),
            size_hint=(1, None),
            height=55
        )

        self.root_layout.add_widget(self.title_label)

        # -------------------------------------------------
        # INPUT GRID
        # -------------------------------------------------

        input_grid = GridLayout(
            cols=2,
            spacing=8,
            size_hint=(1, None)
        )

        input_grid.bind(
            minimum_height=input_grid.setter("height")
        )

        # Input fields
        self.id_input = TextInput(
            hint_text="Book ID",
            multiline=False,
            size_hint_y=None,
            height=42,
            font_size=17,
            foreground_color=(0.05, 0.15, 0.45, 1)
        )

        self.title_input = TextInput(
            hint_text="Book Title",
            multiline=False,
            size_hint_y=None,
            height=42,
            font_size=17,
            foreground_color=(0.05, 0.15, 0.45, 1)
        )

        self.author_input = TextInput(
            hint_text="Author",
            multiline=False,
            size_hint_y=None,
            height=42,
            font_size=17,
            foreground_color=(0.05, 0.15, 0.45, 1)
        )

        self.price_input = TextInput(
            hint_text="Price",
            multiline=False,
            size_hint_y=None,
            height=42,
            font_size=17,
            foreground_color=(0.05, 0.15, 0.45, 1)
        )

        self.year_input = TextInput(
            hint_text="Year",
            multiline=False,
            size_hint_y=None,
            height=42,
            font_size=17,
            foreground_color=(0.05, 0.15, 0.45, 1)
        )

        self.publisher_input = TextInput(
            hint_text="Publisher",
            multiline=False,
            size_hint_y=None,
            height=42,
            font_size=17,
            foreground_color=(0.05, 0.15, 0.45, 1)
        )

        # Labels
        label_color = (0.05, 0.15, 0.45, 1)

        input_grid.add_widget(
            Label(
                text="ID:",
                color=label_color,
                font_size=18,
                bold=True,
                size_hint_y=None,
                height=42
            )
        )

        input_grid.add_widget(self.id_input)

        input_grid.add_widget(
            Label(
                text="Title:",
                color=label_color,
                font_size=18,
                bold=True,
                size_hint_y=None,
                height=42
            )
        )

        input_grid.add_widget(self.title_input)

        input_grid.add_widget(
            Label(
                text="Author:",
                color=label_color,
                font_size=18,
                bold=True,
                size_hint_y=None,
                height=42
            )
        )

        input_grid.add_widget(self.author_input)

        input_grid.add_widget(
            Label(
                text="Price:",
                color=label_color,
                font_size=18,
                bold=True,
                size_hint_y=None,
                height=42
            )
        )

        input_grid.add_widget(self.price_input)

        input_grid.add_widget(
            Label(
                text="Year:",
                color=label_color,
                font_size=18,
                bold=True,
                size_hint_y=None,
                height=42
            )
        )

        input_grid.add_widget(self.year_input)

        input_grid.add_widget(
            Label(
                text="Publisher:",
                color=label_color,
                font_size=18,
                bold=True,
                size_hint_y=None,
                height=42
            )
        )

        input_grid.add_widget(self.publisher_input)

        self.root_layout.add_widget(input_grid)

        # -------------------------------------------------
        # BUTTON ROW 1
        # -------------------------------------------------

        btn_layout1 = BoxLayout(
            size_hint_y=None,
            height=55,
            spacing=10
        )

        btn_layout1.add_widget(
            Button(
                text="ADD",
                font_size=17,
                bold=True,
                background_color=(0.0, 0.45, 0.15, 1),
                color=(1, 1, 1, 1),
                on_press=self.add_book
            )
        )

        btn_layout1.add_widget(
            Button(
                text="SHOW",
                font_size=17,
                bold=True,
                background_color=(0.05, 0.35, 0.70, 1),
                color=(1, 1, 1, 1),
                on_press=self.show_books
            )
        )

        btn_layout1.add_widget(
            Button(
                text="SEARCH",
                font_size=17,
                bold=True,
                background_color=(0.85, 0.55, 0.0, 1),
                color=(1, 1, 1, 1),
                on_press=self.search_book
            )
        )

        btn_layout1.add_widget(
            Button(
                text="DELETE",
                font_size=17,
                bold=True,
                background_color=(0.75, 0.05, 0.05, 1),
                color=(1, 1, 1, 1),
                on_press=self.delete_book
            )
        )

        self.root_layout.add_widget(btn_layout1)

        # -------------------------------------------------
        # BUTTON ROW 2
        # -------------------------------------------------

        btn_layout2 = BoxLayout(
            size_hint_y=None,
            height=55,
            spacing=10
        )

        btn_layout2.add_widget(
            Button(
                text="UPDATE",
                font_size=17,
                bold=True,
                background_color=(0.35, 0.10, 0.60, 1),
                color=(1, 1, 1, 1),
                on_press=self.update_book
            )
        )

        btn_layout2.add_widget(
            Button(
                text="COUNT",
                font_size=17,
                bold=True,
                background_color=(0.0, 0.45, 0.45, 1),
                color=(1, 1, 1, 1),
                on_press=self.count_books
            )
        )

        btn_layout2.add_widget(
            Button(
                text="CLEAR ALL",
                font_size=17,
                bold=True,
                background_color=(0.25, 0.25, 0.30, 1),
                color=(1, 1, 1, 1),
                on_press=self.clear_all
            )
        )

        self.root_layout.add_widget(btn_layout2)

        # -------------------------------------------------
        # OUTPUT AREA
        # -------------------------------------------------

        self.output = Label(
            text="Welcome to Library App",
            font_size=18,
            color=(0.03, 0.18, 0.65, 1),
            size_hint_y=None,
            height=400,
            markup=True,
            halign="left",
            valign="top"
        )

        # Make text wrap according to screen width
        self.output.bind(
            width=lambda instance, value:
            setattr(instance, "text_size", (value, None))
        )

        scroll = ScrollView(
            size_hint=(1, 1)
        )

        scroll.add_widget(self.output)

        self.root_layout.add_widget(scroll)

        return self.root_layout

    # -------------------------------------------------
    # ADD BOOK
    # -------------------------------------------------

    def add_book(self, instance):

        book = {
            "id": self.id_input.text,
            "title": self.title_input.text,
            "author": self.author_input.text,
            "price": self.price_input.text,
            "year": self.year_input.text,
            "publisher": self.publisher_input.text
        }

        if not book["id"] or not book["title"]:
            self.output.text = "[b]Please enter Book ID and Title.[/b]"
            return

        library.append(book)

        save_books()

        self.output.text = (
            f"[b]BOOK ADDED SUCCESSFULLY[/b]\n\n"
            f"ID: {book['id']}\n"
            f"Title: {book['title']}\n"
            f"Author: {book['author']}\n"
            f"Price: {book['price']}\n"
            f"Year: {book['year']}\n"
            f"Publisher: {book['publisher']}"
        )

        self.clear_inputs()

    # -------------------------------------------------
    # SHOW BOOKS
    # -------------------------------------------------

    def show_books(self, instance):

        if not library:

            self.output.text = "[b]No books available.[/b]"

        else:

            books_list = "\n\n".join(
                [
                    f"[b]ID:[/b] {b['id']}\n"
                    f"[b]Title:[/b] {b['title']}\n"
                    f"[b]Author:[/b] {b['author']}\n"
                    f"[b]Price:[/b] {b['price']}\n"
                    f"[b]Year:[/b] {b['year']}\n"
                    f"[b]Publisher:[/b] {b['publisher']}"
                    for b in library
                ]
            )

            self.output.text = (
                f"[b]BOOKS IN LIBRARY[/b]\n\n"
                f"{books_list}"
            )

    # -------------------------------------------------
    # SEARCH BOOK
    # -------------------------------------------------

    def search_book(self, instance):

        search_id = self.id_input.text

        for b in library:

            if b["id"] == search_id:

                self.output.text = (
                    f"[b]BOOK FOUND[/b]\n\n"
                    f"[b]ID:[/b] {b['id']}\n"
                    f"[b]Title:[/b] {b['title']}\n"
                    f"[b]Author:[/b] {b['author']}\n"
                    f"[b]Price:[/b] {b['price']}\n"
                    f"[b]Year:[/b] {b['year']}\n"
                    f"[b]Publisher:[/b] {b['publisher']}"
                )

                return

        self.output.text = "[b]BOOK NOT FOUND[/b]"

    # -------------------------------------------------
    # DELETE BOOK
    # -------------------------------------------------

    def delete_book(self, instance):

        search_id = self.id_input.text

        for b in library:

            if b["id"] == search_id:

                library.remove(b)

                save_books()

                self.output.text = (
                    f"[b]BOOK DELETED SUCCESSFULLY[/b]\n\n"
                    f"Title: {b['title']}"
                )

                self.clear_inputs()

                return

        self.output.text = "[b]BOOK NOT FOUND[/b]"

    # -------------------------------------------------
    # UPDATE BOOK
    # -------------------------------------------------

    def update_book(self, instance):

        search_id = self.id_input.text

        for b in library:

            if b["id"] == search_id:

                if self.title_input.text:
                    b["title"] = self.title_input.text

                if self.author_input.text:
                    b["author"] = self.author_input.text

                if self.price_input.text:
                    b["price"] = self.price_input.text

                if self.year_input.text:
                    b["year"] = self.year_input.text

                if self.publisher_input.text:
                    b["publisher"] = self.publisher_input.text

                save_books()

                self.output.text = (
                    f"[b]BOOK UPDATED SUCCESSFULLY[/b]\n\n"
                    f"Title: {b['title']}\n"
                    f"Year: {b['year']}"
                )

                self.clear_inputs()

                return

        self.output.text = "[b]BOOK NOT FOUND[/b]"

    # -------------------------------------------------
    # COUNT BOOKS
    # -------------------------------------------------

    def count_books(self, instance):

        total = len(library)

        self.output.text = (
            f"[b]TOTAL BOOKS IN LIBRARY[/b]\n\n"
            f"{total}"
        )

    # -------------------------------------------------
    # CLEAR ALL
    # -------------------------------------------------

    def clear_all(self, instance):

        library.clear()

        save_books()

        self.output.text = (
            "[b]LIBRARY CLEARED SUCCESSFULLY![/b]"
        )

    # -------------------------------------------------
    # CLEAR INPUTS
    # -------------------------------------------------

    def clear_inputs(self):

        self.id_input.text = ""
        self.title_input.text = ""
        self.author_input.text = ""
        self.price_input.text = ""
        self.year_input.text = ""
        self.publisher_input.text = ""


# -------------------------------------------------
# RUN APPLICATION
# -------------------------------------------------

if __name__ == "__main__":
    LibraryApp().run()