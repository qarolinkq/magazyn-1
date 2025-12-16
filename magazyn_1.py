import streamlit as st

# --- 1. Zarządzanie Stanem Sesji (Session State Management) ---

# Inicjalizacja stanu sesji
if 'produkty' not in st.session_state:
    st.session_state['produkty'] = [] 

# --- 2. Funkcje Logiki (Callbacks) ---

def dodaj_produkt():
    """Dodaje produkt do listy i czyści pole tekstowe."""
    nazwa_produktu = st.session_state.nowy_produkt.strip()
    if nazwa_produktu: 
        st.session_state.produkty.append(nazwa_produktu)
        st.session_state.nowy_produkt = "" 

def usun_produkt(produkt_do_usuniecia):
    """Usuwa podany produkt z listy."""
    try:
        st.session_state.produkty.remove(produkt_do_usuniecia)
    except ValueError:
        st.error(f"Wystąpił błąd podczas usuwania: {produkt_do_usuniecia}")


# --- 3. Główna Funkcja Aplikacji (Streamlit App Layout) ---

# --- DODANIE MIKOŁAJA NA PASKU BOCZNYM (st.sidebar) ---

with st.sidebar:
    st.title("🎄 Święta w Magazynie!")
    st.image(
        "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png", # Zastąp to obrazkiem Mikołaja, np. z publicznego źródła
        caption="Pomoce Mikołaja gotowe do pracy",
        width=150
    )
    # Prosty Mikołaj w postaci emoji:
    st.markdown("""
        ## 🎅 Mikołaj Czuwa
        
        Witaj w magazynie! Pamiętaj, aby wszystkie prezenty (produkty)
        zostały dodane i usunięte z listy.
        
        Hoł, Hoł, Hoł!
    """)
    st.markdown("---")
    # Można tu dodać np. statystyki:
    st.info(f"Aktualnie w magazynie: **{len(st.session_state.produkty)}** produktów.")


# --- Główna Treść Aplikacji ---
def main():
    st.title("📦 Prosta Aplikacja Magazynowa")
    st.markdown("Dodaj lub usuń produkty z listy. Stan jest przechowywany w pamięci (sesji przeglądarki).")

    # Sekcja Dodawania Produktu
    st.header("➕ Dodaj Produkt")
    
    with st.container():
        st.text_input(
            "Nazwa nowego produktu",
            key="nowy_produkt",
            on_change=dodaj_produkt,
            placeholder="Wprowadź nazwę produktu i naciśnij Enter"
        )
        st.button("Dodaj ręcznie", on_click=dodaj_produkt)

    # Separator
    st.markdown("---")

    # Sekcja Wyświetlania Produktów
    st.header("🗒️ Lista Produktów w Magazynie")

    if st.session_state.produkty:
        # Tworzymy nagłówki wizualnie
        st.markdown("**Lp.** | **Nazwa Produktu** | **Akcja**")
        
        # Wyświetlanie produktów
        for i, produkt in enumerate(st.session_state.produkty):
            col1, col2, col3 = st.columns([0.1, 0.7, 0.2]) # Zmieniony układ kolumn
            
            with col1:
                st.write(f"*{i+1}.*")
                
            with col2:
                st.write(f"**{produkt}**")
                
            with col3:
                st.button(
                    "Usuń",
                    key=f"delete_btn_{i}",
                    on_click=usun_produkt,
                    args=(produkt,),
                    type="secondary"
                )
    else:
        st.info("Magazyn jest pusty. Mikołaj czeka na prezenty!")

    st.markdown("---")
    st.caption("Aplikacja oparta o Streamlit i prostą listę w pamięci. Dane tracone po zamknięciu sesji.")

# Zabezpieczenie uruchomienia
if __name__ == "__main__":
    main()
