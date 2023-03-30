fetch("http://127.0.0.1/message/3")
  .then((r) => r.text())
  .then((r) => {
    fetch("http://127.0.0.1/submit", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: r }),
    })
      .then((r) => r.text())
      .then((r) => alert(r));
  });
