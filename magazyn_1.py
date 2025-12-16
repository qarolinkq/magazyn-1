import streamlit as st

# Ustawienie szerokości paska bocznego na 0, aby skupić się na głównym widoku
# st.set_page_config(layout="wide") # Opcjonalnie: ustawia szeroki widok

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


# --- 2. Główna Funkcja Aplikacji (Streamlit App Layout) ---

def main():
    st.title("📦 Prosta Aplikacja Magazynowa")
    st.markdown("Dodaj lub usuń produkty z listy. Stan jest przechowywany w pamięci (sesji przeglądarki).")
    
    # --- NOWA STRUKTURA: Mikołaj w lewej kolumnie, Dodawanie w prawej ---
    
    # Dzielimy główny obszar na dwie kolumny (np. 1:2)
    col_mikolaj, col_dodaj = st.columns([1, 2])
    
    with col_mikolaj:
        st.markdown("# 🎅") # Duży symbol Mikołaja
        st.header("Kontrola Świąteczna")
        st.markdown("""
            **HOŁ, HOŁ, HOŁ!**
            
            Magazyn jest gotowy.
            
            Aktualnie: **{len(st.session_state.produkty)}** prezentów.
        """)
        
    with col_dodaj:
        st.header("➕ Dodaj Produkt")
        st.text_input(
            "Nazwa nowego produktu/prezentu",
            key="nowy_produkt",
            on_change=dodaj_produkt,
            placeholder="Wprowadź nazwę i naciśnij Enter"
        )
        st.button("Dodaj do listy", on_click=dodaj_produkt)

    # --- Separator ---
    st.markdown("---")

    # --- Sekcja Wyświetlania Produktów (Pełna Szerokość) ---
    st.header("🗒️ Lista Produktów w Magazynie")

    if st.session_state.produkty:
        # Tabela (mniej więcej)
        st.markdown("**Lp.** | **Nazwa Produktu** | **Akcja**")
        
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
    st.caption("Aplikacja oparta o Streamlit i prostą listę w pamięci.")

if __name__ == "__main__":
    main()
