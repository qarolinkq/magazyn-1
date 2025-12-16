import streamlit as st

# --- 1. Zarządzanie Stanem Sesji (Session State Management) ---

if 'produkty' not in st.session_state:
    st.session_state['produkty'] = [] 

def dodaj_produkt():
    nazwa_produktu = st.session_state.nowy_produkt.strip()
    if nazwa_produktu: 
        st.session_state.produkty.append(nazwa_produktu)
        st.session_state.nowy_produkt = "" 

def usun_produkt(produkt_do_usuniecia):
    try:
        st.session_state.produkty.remove(produkt_do_usuniecia)
    except ValueError:
        st.error(f"Wystąpił błąd podczas usuwania: {produkt_do_usuniecia}")


# --- 3. Główna Funkcja Aplikacji (Streamlit App Layout) ---

# --- BARDZO DUŻY MIKOŁAJ NA PASKU BOCZNYM (st.sidebar) ---

with st.sidebar:
    # Użycie nagłówka H1 i dużego emoji, aby Mikołaj był "duży"
    st.markdown("# 🎅") # Duży symbol Mikołaja
    st.markdown("---")
    
    st.title("🎄 Magazyn Świąteczny")
    
    st.markdown("""
        ### Kontrola Mikołaja
        
        **HOŁ, HOŁ, HOŁ!** Upewnij się, że lista prezentów jest aktualna.
        Żadne dziecko nie może zostać pominięte!
    """)
    
    # Możemy też użyć st.image z większą szerokością
    # st.image(
    #     "https://i.imgur.com/example-santa.png", # Zastąp faktycznym publicznym obrazkiem
    #     width=250 # Większa szerokość
    # )
    
    st.markdown("---")
    st.info(f"Aktualnie w magazynie: **{len(st.session_state.produkty)}** prezentów.")


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
            placeholder="Wprowadź nazwę produktu/prezentu i naciśnij Enter"
        )
        st.button("Dodaj ręcznie", on_click=dodaj_produkt)

    # Separator
    st.markdown("---")

    # Sekcja Wyświetlania Produktów
    st.header("🗒️ Lista Produktów w Magazynie")

    if st.session_state.produkty:
        st.markdown("**Lp.** | **Nazwa Produktu** | **Akcja**")
        
        # Wyświetlanie produktów
        for i, produkt in enumerate(st.session_state.produkty):
            col1, col2, col3 = st.columns([0.1, 0.7, 0.2]) 
            
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

if __name__ == "__main__":
    main()
