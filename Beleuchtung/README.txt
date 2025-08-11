Ziel dieses Projekts war die Entwicklung einer Beleuchtung für ein Modellhaus, bestehend aus acht Paaren weißer LEDs. Die Ansteuerung erfolgt über einen Raspberry Pi Pico W, der mithilfe einer 4x4-Tastermatrix bedient wird.

Es stehen drei Beleuchtungsmodi zur Verfügung:

Modus A – Alle LEDs blinken synchron mit einer Frequenz von 5 Hz.

Modus B – Zufällig ausgewählte LED-Paare blinken mit einer Frequenz von 20 Hz.

Modus C – Die LED-Paare können einzeln über die Nummerntasten 1–8 der Matrix ein- und ausgeschaltet werden.

Zusätzlich kann über Taste D ein kompletter Aus-Zustand aktiviert werden, der alle LEDs ausschaltet.

Die LED-Paare werden über eine 9-V-Batterie mit Strom versorgt, während der Pico über eine Powerbank betrieben wird. Zum Schalten der LEDs kommt ein ULN2803A-Treiberbaustein zum Einsatz, der den Stromfluss zu den einzelnen Paaren ein- oder ausschaltet.

