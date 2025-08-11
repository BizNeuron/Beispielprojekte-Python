Um die Grundlagen von Threads, Sockets und SQL-Datenbanken zu erlernen, habe ich dieses Projekt als simplen Prototypen entwickelt. Ziel ist es, einen einfachen Server zu simulieren, der Benutzerprofile in einer Datenbank verwaltet.
Die Hauptfunktionen sind das Erstellen eines neuen Accounts sowie das Einloggen in einen bestehenden.

Account-Erstellung:
Zunächst übermittelt der Client (z. B. der PC eines Nutzers) die für das Benutzerprofil erforderlichen Daten an den Server. Anschließend sendet der Server an die angegebene E-Mail-Adresse eine Nachricht mit einem Bestätigungscode. Der Benutzer gibt diesen Code in den Client ein, der ihn wiederum an den Server überträgt. Ist der Code korrekt, wird das Profil in der Datenbank angelegt.

Login:
Für den Login übermittelt der Client den Benutzernamen, die E-Mail-Adresse und das Passwort an den Server. Stimmen die Angaben mit den gespeicherten Daten überein und entspricht das eingegebene Passwort der verschlüsselten Version in der Datenbank, erhält der Benutzer Zugriff auf seinen Account.
