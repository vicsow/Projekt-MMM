# Projekt: Symulator Układu z Realizowalnym Sterownikiem PID

## 1. Opis Projektu
Celem projektu jest implementacja symulatora układu dynamicznego opisanego transmitancją drugiego stopnia wraz z realizowalnym sterownikiem PID w konfiguracji z ujemnym sprzężeniem zwrotnym.
Program wyświetla odpowiedź układu o dowolnie zadanych parametrachach obiektu i PID.

### Model Matematyczny Obiektu
Układ (obiekt) jest opisany transmitancją operatorową:
$$G_o(s) = \frac{a_1s + a_0}{b_2s^2 + b_1s + b_0}$$

### Sterownik PID
Zaimplementowano **realizowalny sterownik PID**. W odróżnieniu od idealnego PID, człon różniczkujący posiada dodatkową filtrację (inercję), co pozwala na jego fizyczną realizację w systemach cyfrowych i ogranicza wpływ szumów wysokoczęstotliwościowych. Jego transmitancja wynosi $G_{PID} = K_p*(1 + \frac{1}{T_d*s} + \frac{T_i*s}{1+T_f*s})$

## 2. Funkcje Symulatora
Symulator umożliwia generowanie i analizę odpowiedzi układu dla trzech rodzajów pobudzeń wejściowych:
1.  **Sygnał Prostokątny** – o skończonym czasie trwania.
2.  **Sygnał Trójkątny** – (sawtooth/triangle).
3.  **Sygnał Harmoniczny** – (sinusoidalny).

Program pozwala na swobodną zmianę parametrów:
* Współczynników transmitancji: $a_1, a_0, b_2, b_1, b_0$.
* Nastaw regulatora PID: $K_p, T_i, T_d$ oraz stałej czasowej filtra $T_f$.
* Parametrów sygnałów wejściowych (amplituda, częstotliwość, wypełnienie).

## 3. Implementacja Techniczna
Do obliczeń numerycznych wykorzystano metodę całkowania **trapezów**, która zapewnia dobrą stabilność i dokładność odwzorowania sygnałów ciągłych w dziedzinie czasu dyskretnego.

### Wymagania systemowe
Do uruchomienia projektu wymagany jest Python 3.x oraz biblioteki:
* `numpy` – obliczenia macierzowe i matematyczne.
* `scipy` – generowanie sygnałów okresowych.
* `matplotlib` – wizualizacja wyników (wykresy).
