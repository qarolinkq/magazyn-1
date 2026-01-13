import streamlit as st

# --- 1. Zarządzanie Stanem Sesji (Session State) ---

# Inicjalizacja słownika produktów { "Nazwa": ilość }
if 'produkty_dict' not in st.session_state:
    st.session_state['produkty_dict'] = {}

def dodaj_produkt():
    nazwa = st.session_state.nowy_produkt.strip()
    ilosc = st.session_state.ilosc_dodaj
    if nazwa:
        # Jeśli produkt istnieje, dodaj do obecnej ilości, jeśli nie - stwórz nowy
        if nazwa in st.session_state.produkty_dict:
            st.session_state.produkty_dict[nazwa] += ilosc
        else:
            st.session_state.produkty_dict[nazwa] = ilosc
        # Czyszczenie pól po dodaniu
        st.session_state.nowy_produkt = ""
        st.session_state.ilosc_dodaj = 1

def usun_ilosc(nazwa, ilosc_do_odjecia):
    if nazwa in st.session_state.produkty_dict:
        # Odejmij wybraną ilość
        st.session_state.produkty_dict[nazwa] -= ilosc_do_odjecia
        # Jeśli ilość spadnie do 0 lub mniej, usuń produkt całkowicie
        if st.session_state.produkty_dict[nazwa] <= 0:
            del st.session_state.produkty_dict[nazwa]

# --- 2. Układ Aplikacji (Layout) ---

def main():
    st.set_page_config(page_title="Magazyn Mikołaja", layout="wide")
    st.title("📦 Zaawansowany Magazyn Prezentów")
    
    # --- Sekcja Góra: Mikołaj i Dodawanie ---
    col_mikolaj, col_dodaj = st.columns([1, 2])
    
    with col_mikolaj:
        st.markdown("# 🎅")
        st.header("Kontrola Świąteczna")
        laczna_suma = sum(st.session_state.produkty_dict.values())
        st.markdown(f"""
            **HOŁ, HOŁ, HOŁ!**
            Aktualnie w magazynie masz:
            ## {laczna_suma} 
            prezentów łącznie.
        """)
        
    with col_dodaj:
        st.header("➕ Przyjęcie Towaru")
        c1, c2 = st.columns([3, 1])
        with c1:
            st.text_input("Co chcesz dodać?", key="nowy_produkt", placeholder="Wpisz nazwę...")
        with c2:
            st.number_input("Ile sztuk?", min_value=1, value=1, key="ilosc_dodaj")
        
        st.button("Dodaj do magazynu", on_click=dodaj_produkt, use_container_width=True)

    st.markdown("---")

    # --- Sekcja Dół: Lista i Wydawanie ---
    st.header("🗒️ Aktualny Stan i Wydawanie z Magazynu")

    if st.session_state.produkty_dict:
        # Nagłówki "tabeli"
        h1, h2, h3, h4 = st.columns([0.4, 0.2, 0.2, 0.2])
        h1.write("**Nazwa Produktu**")
        h2.write("**W magazynie**")
        h3.write("**Ilość do odjęcia**")
        h4.write("**Akcja**")
        
        # Iterujemy po produktach w słowniku
        for nazwa, stan in list(st.session_state.produkty_dict.items()):
            col_nazwa, col_stan, col_input, col_btn = st.columns([0.4, 0.2, 0.2, 0.2])
            
            with col_nazwa:
                st.write(f"**{nazwa}**")
            
            with col_stan:
                st.write(f"{stan} szt.")
            
            with col_input:
                # Pole pozwalające wybrać, ile sztuk chcemy usunąć
                ile_odjac = st.number_input(
                    "Ile usunąć?", 
                    min_value=1, 
                    max_value=stan, # Nie pozwoli usunąć więcej niż jest w magazynie
                    value=1, 
                    key=f"del_val_{nazwa}",
                    label_visibility="collapsed"
                )
            
            with col_btn:
                st.button(
                    "Odejmij / Usuń", 
                    key=f"del_btn_{nazwa}", 
                    on_click=usun_ilosc, 
                    args=(nazwa, ile_odjac),
                    type="primary"
                )
    else:
        st.info("Magazyn jest pusty. Mikołaj czeka na dostawę!")

    st.markdown("---")
    st.caption("Dane są zapisane w sesji (znikną po odświeżeniu strony w przeglądarce).")

if __name__ == "__main__":
    main()
