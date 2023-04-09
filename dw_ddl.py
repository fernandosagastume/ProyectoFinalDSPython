DDL_QUERY =  '''
CREATE TABLE cliente (
    idCliente INT PRIMARY KEY,
    gender VARCHAR(10) NOT NULL,
    customer_type VARCHAR(50) NOT NULL,
    age INT NOT NULL
);
CREATE TABLE viaje (
    idViaje INT PRIMARY KEY,
    flight_distance INT NOT NULL,
    travel_type VARCHAR(20) NOT NULL,
    class VARCHAR(20) NOT NULL
);
CREATE TABLE servicio (
    idServicio INT PRIMARY KEY,
    wifi_service INT NOT NULL,
    ease_of_online_booking INT NOT NULL,
    gate_location INT NOT NULL,
    food_and_drink INT NOT NULL,
    online_boarding INT NOT NULL,
    seat_comfort INT NOT NULL,
    inflight_entertainment INT NOT NULL,
    on_board_service INT NOT NULL,
    leg_room_service INT NOT NULL,
    baggage_handling INT NOT NULL,
    checkin_service INT NOT NULL,
    inflight_service INT NOT NULL,
    cleanliness INT NOT NULL
);
CREATE TABLE aeropuerto (
  idAeropuerto INTEGER PRIMARY KEY,
  airportName VARCHAR(100) NOT NULL,
  airportCode CHAR(5) NOT NULL
);
CREATE TABLE viaje_satisfaccion (
  idCliente INTEGER,
  idViaje INTEGER,
  idServicio INTEGER,
  idAeropuerto INTEGER,
  satisfaction VARCHAR(45) NOT NULL,
  DepartureDelay INTEGER NOT NULL,
  ArrivalDelay DECIMAL(10,2) NOT NULL,
  FOREIGN KEY (idCliente) REFERENCES cliente (idCliente),
  FOREIGN KEY (idViaje) REFERENCES viaje (idViaje),
  FOREIGN KEY (idServicio) REFERENCES servicio (idServicio),
  FOREIGN KEY (idAeropuerto) REFERENCES aeropuerto (idAeropuerto)
);

'''