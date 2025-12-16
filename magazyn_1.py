import streamlit as st

# Inicjalizacja stanu sesji dla listy produktów
# Używamy st.session_state do przechowywania danych w Streamlit
if 'produkty' not in st.session_state:
    st.session_state['produkty'] = [] # Pusta lista na nazwy produktów

def dodaj_produkt():
    """Dodaje produkt do listy na podstawie wartości z pola tekstowego."""
    nazwa_produktu = st.session_state.nowy_produkt.strip()
    if nazwa_produktu: # Sprawdzamy, czy pole nie jest puste
        st.session_state.produkty.append(nazwa_produktu)
        st.session_state.nowy_produkt = "" # Czyścimy pole po dodaniu

def usun_produkt(produkt_do_usuniecia):
    """Usuwa podany produkt z listy."""
    try:
        st.session_state.produkty.remove(produkt_do_usuniecia)
    except ValueError:
        # Ten wyjątek jest mało prawdopodobny w tym kontekście, ale zabezpiecza na wypadek
        st.error(f"Nie udało się usunąć produktu: {produkt_do_usuniecia}")


# --- Interfejs Użytkownika ---

st.title("📦 Prosta Aplikacja Magazynowa")
st.markdown("Dodaj lub usuń produkty z listy. Bez cen i ilości.")

# --- Sekcja Dodawania Produktu ---
st.header("➕ Dodaj Produkt")
st.text_input(
    "Nazwa nowego produktu",
    key="nowy_produkt", # Klucz do pobrania wartości
    on_change=dodaj_produkt, # Funkcja wywoływana po naciśnięciu Enter lub kliknięciu poza polem
    placeholder="Wprowadź nazwę produktu i naciśnij Enter"
)

st.button("Dodaj", on_click=dodaj_produkt)


# --- Sekcja Wyświetlania Produktów ---
st.header("🗒️ Lista Produktów w Magazynie")

if st.session_state.produkty:
    # Wyświetlamy produkty i przyciski do usuwania
    for i, produkt in enumerate(st.session_state.produkty):
        # Używamy st.columns do ułożenia nazwy i przycisku w jednym wierszu
        col1, col2 = st.columns([0.8, 0.2])
        
        with col1:
            st.write(f"**{i+1}.** {produkt}")
            
        with col2:
            # Tworzymy unikatowy klucz dla każdego przycisku, używając indeksu
            st.button(
                "Usuń",
                key=f"delete_btn_{i}",
                on_click=usun_produkt,
                args=(produkt,), # Argument przekazywany do funkcji usun_produkt
                type="secondary" # Wyróżnienie przycisku
            )
else:
    st.info("Magazyn jest pusty. Dodaj pierwszy produkt!")

# --- Stopka ---
st.markdown("---")
st.caption("Aplikacja oparta o Streamlit i prostą listę w pamięci.")
