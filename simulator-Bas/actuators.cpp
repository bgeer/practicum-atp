#include <pybind11/pybind11.h>
#include <iostream>

namespace py = pybind11;

class Relay {
protected:
    bool state;
    
public:
    Relay() : state(false) {}

    virtual void on() {
        state = true;
    }

    virtual void off() {
        state = false;
    }

    virtual bool get_state() const {
        return state;
    }
};

class Heater : public Relay {
public:
    void on() override {
        Relay::on();
        std::cout << "Heater turned on" << std::endl;
    }

    void off() override {
        Relay::off();
        std::cout << "Heater turned off" << std::endl;
    }
};

class Pump : public Relay {
public:
    void on() override {
        Relay::on();
        std::cout << "Pump turned on" << std::endl;
    }

    void off() override {
        Relay::off();
        std::cout << "Pump turned off" << std::endl;
    }
};


PYBIND11_MODULE(actuators, m) {
    pybind11::class_<Relay>(m, "Relay")
        .def(pybind11::init<>())
        .def("on", &Relay::on)
        .def("off", &Relay::off)
        .def("get_state", &Relay::get_state);

    pybind11::class_<Heater, Relay>(m, "Heater")
        .def(pybind11::init<>())
        .def("on", &Heater::on)
        .def("off", &Heater::off);

    pybind11::class_<Pump, Relay>(m, "Pump")
        .def(pybind11::init<>())
        .def("on", &Pump::on)
        .def("off", &Pump::off);
}