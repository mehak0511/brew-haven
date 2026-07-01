const form = document.getElementById("reservationForm");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const reservation = {
        full_name: document.getElementById("full_name").value,
        email: document.getElementById("email").value,
        phone: document.getElementById("phone").value,
        guests: Number(document.getElementById("guests").value),
        reservation_date: document.getElementById("reservation_date").value,
        reservation_time: document.getElementById("reservation_time").value,
        occasion: document.getElementById("occasion").value,
        special_request: document.getElementById("special_request").value
    };

    try {
        const response = await fetch("http://127.0.0.1:8000/reservations", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(reservation)
        });

        if (response.ok) {
            alert("🎉 Reservation Confirmed!");
            form.reset();
        } else {
            const error = await response.json();
            console.log(error);
            alert("Reservation failed.");
        }

    } catch (err) {
        console.error(err);
        alert("Cannot connect to server.");
    }

});

    