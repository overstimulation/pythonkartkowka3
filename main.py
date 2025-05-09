import datetime

import matplotlib.pyplot as plt

# --- Sekcja 1: Przygotowanie Danych ---
# Tutaj wczytaj swoje dane lub wygeneruj przykładowe.
# Pamiętaj o odpowiednim formacie danych dla osi X i Y.
# Możesz używać list, tupli, czy słowników.

# Przykładowe dane liczbowe:
x_data_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_data_num_1 = [10, 12, 8, 15, 11, 9, 13, 16, 14, 18]
y_data_num_2 = [5, 7, 4, 9, 6, 5, 8, 10, 7, 11]

# Przykładowe dane kategorialne (dla osi X lub wykresów słupkowych/kołowych):
categories = ["Jabłka", "Banany", "Pomarańcze", "Winogrona"]
values_category = [35, 20, 30, 15]  # Wartości odpowiadające kategoriom

# Przykładowe dane czasowe:
time_strings = ["2023-01-01 12:00", "2023-01-01 13:00", "2023-01-01 14:00", "2023-01-01 15:00"]
x_data_time = [datetime.datetime.strptime(ts, "%Y-%m-%d %H:%M") for ts in time_strings]
y_data_time_values = [5, 6, 7, 8]

# Przykładowe dane dla histogramu (lista wartości, których rozkład chcemy zobaczyć):
histogram_data = [1, 1, 2, 3, 3, 3, 4, 5, 5, 6, 7, 7, 7, 7, 8, 9, 10]

# --- Sekcja 2: Tworzenie Wykresu (Podstawowe Typy) ---

# Tworzenie pojedynczego wykresu:
fig1, ax1 = plt.subplots(figsize=(8, 6))  # Ustaw rozmiar rysunku

# Wykres liniowy:
ax1.plot(x_data_num, y_data_num_1, label="Seria Liniowa 1", marker="o", linestyle="-", color="blue")
ax1.plot(x_data_num, y_data_num_2, label="Seria Liniowa 2", marker="x", linestyle="--", color="red")

# Wykres słupkowy:
fig2, ax2 = plt.subplots(figsize=(8, 6))
ax2.bar(
    categories, values_category, label="Sprzedaż", color=["skyblue", "lightgreen", "salmon", "gold"]
)  # Kolory dla każdego słupka

# Wykres punktowy (scatter plot):
fig3, ax3 = plt.subplots(figsize=(8, 6))
ax3.scatter(x_data_num, y_data_num_1, label="Punkty Danych", color="purple", marker="^", s=100)  # s - rozmiar punktów

# Wykres kołowy (pie chart) - często używany do pokazywania proporcji:
fig4, ax4 = plt.subplots(figsize=(8, 8))  # Wykres kołowy często lepiej wygląda jako kwadrat
ax4.pie(
    values_category,
    labels=categories,
    autopct="%1.1f%%",
    startangle=90,
    colors=["skyblue", "lightgreen", "salmon", "gold"],
)
ax4.axis("equal")  # Upewnij się, że koło jest okrągłe (Equal aspect ratio ensures that pie is drawn as a circle.)
ax4.set_title("Rozkład Kategorii")  # Tytuł dla wykresu kołowego

# Histogram - pokazuje rozkład częstotliwości danych:
fig5, ax5 = plt.subplots(figsize=(8, 6))
ax5.hist(
    histogram_data, bins=5, edgecolor="black", alpha=0.7
)  # bins - liczba "koszyków", edgecolor - kolor krawędzi słupków
ax5.set_xlabel("Wartość")
ax5.set_ylabel("Częstotliwość")
ax5.set_title("Histogram Danych")


# --- Sekcja 3: Dostosowanie Wykresu ---

# Dostosowanie wykresu liniowego (ax1):
ax1.set_title("Wykres Liniowy z Dwoma Seriami")
ax1.set_xlabel("Oś X (Liczby)")
ax1.set_ylabel("Oś Y (Wartości)")
ax1.legend()  # Dodaj legendę
ax1.grid(True)  # Dodaj siatkę

# Dostosowanie wykresu słupkowego (ax2):
ax2.set_title("Wykres Słupkowy Kategorii")
ax2.set_xlabel("Kategoria")
ax2.set_ylabel("Wartość")
ax2.legend()
ax2.grid(axis="y")  # Siatka tylko na osi Y

# Dostosowanie wykresu punktowego (ax3):
ax3.set_title("Wykres Punktowy")
ax3.set_xlabel("Oś X")
ax3.set_ylabel("Oś Y")
ax3.legend()
ax3.grid(True)

# Formatowanie osi X dla danych czasowych (jeśli używasz wykresu z czasem):
# fig_time, ax_time = plt.subplots(figsize=(8, 6))
# ax_time.plot(x_data_time, y_data_time_values)
# ax_time.set_title('Wykres z Danymi Czasowymi')
# ax_time.set_xlabel('Czas')
# ax_time.set_ylabel('Wartość')
# fig_time.autofmt_xdate() # Automatyczne formatowanie dat na osi X


# Dodawanie pionowych lub poziomych linii/zakresów:
# ax1.axvspan(3, 5, color='yellow', alpha=0.3, label='Zakres 3-5') # Pionowy zakres na ax1
# ax1.axhline(y=10, color='green', linestyle='--', label='Linia odniesienia Y=10') # Pozioma linia na ax1
# ax1.legend() # Aktualizacja legendy po dodaniu linii/zakresów

# Dodawanie tekstu lub adnotacji do wykresu:
# ax1.text(4, 16, 'Wartość maksymalna', fontsize=10, color='purple') # Dodaj tekst w punkcie (4, 16)
# ax1.annotate('Punkt szczególny', xy=(8, 16), xytext=(7, 18),
#              arrowprops=dict(facecolor='black', shrink=0.05),
#              fontsize=10) # Dodaj adnotację ze strzałką

# --- Sekcja 4: Tworzenie Wielu Wykresów na Jednym Rysunku (Subplots) ---

# Przykład siatki 2x2 wykresów:
fig_multi, axes = plt.subplots(2, 2, figsize=(10, 8))  # Siatka 2 wiersze, 2 kolumny

# Dostęp do poszczególnych osi w siatce:
ax_top_left = axes[0, 0]
ax_top_right = axes[0, 1]
ax_bottom_left = axes[1, 0]
ax_bottom_right = axes[1, 1]

# Rysowanie na poszczególnych osiach:
ax_top_left.plot(x_data_num, y_data_num_1)
ax_top_left.set_title("Górny Lewy")
ax_top_left.grid(True)

ax_top_right.bar(categories, values_category)
ax_top_right.set_title("Górny Prawy")
ax_top_right.tick_params(axis="x", rotation=45)  # Obróć etykiety na osi X

ax_bottom_left.scatter(x_data_num, y_data_num_2)
ax_bottom_left.set_title("Dolny Lewy")
ax_bottom_left.set_xlabel("Oś X")  # Etykieta X na dolnym wykresie
ax_bottom_left.set_ylabel("Oś Y")  # Etykieta Y na dolnym wykresie
ax_bottom_left.grid(True)

# Możesz zostawić jeden wykres pusty lub dodać inny typ
# ax_bottom_right.hist(histogram_data, bins=7)
# ax_bottom_right.set_title('Dolny Prawy')

# Upewnij się, że etykiety się nie nakładają:
fig_multi.tight_layout()  # Automatyczne dopasowanie układu


# --- Sekcja 5: Zapis lub Wyświetlenie Wykresu ---

# Zapis do pliku (możesz zapisać każdy z wykresów fig1, fig2, ... fig_multi):
fig1.savefig("wykres_liniowy.png", dpi=300, bbox_inches="tight")
fig2.savefig("wykres_slupkowy.pdf", bbox_inches="tight")  # Zapis jako PDF
fig4.savefig("wykres_kolowy.jpg", dpi=300, bbox_inches="tight")
fig_multi.savefig("wiele_wykresow.png", dpi=300, bbox_inches="tight")


# Wyświetlenie wszystkich utworzonych wykresów (użyj tylko jeśli uruchamiasz skrypt lokalnie):
# plt.show()

# Pamiętaj, aby dostosować ten szablon do konkretnych wymagań zadania na kartkówce.
# Kluczowe jest zrozumienie, jakie dane masz i jaki typ wykresu najlepiej je zaprezentuje.
# Komentuj sekcje, których nie używasz, aby kod był czysty.
