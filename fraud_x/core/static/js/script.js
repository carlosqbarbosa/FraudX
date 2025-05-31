// document.getElementById("fraudForm").addEventListener("submit", function(event) {
//     event.preventDefault();  // Impede que a página recarregue

//     let formData = new FormData(this);

//     fetch("{% url 'verify_transaction' %}", {
//         method: "POST",
//         body: formData,
//     })
//     .then(response => response.json())
//     .then(data => {
//         document.getElementById("fraudResult").innerText = data.message;

//         // 🧹 Limpa os campos do formulário
//         this.reset();
//     })
//     .catch(error => console.error("Erro ao enviar formulário:", error));
// });


// // document.getElementById("fraudForm").addEventListener("submit", function(event) {
// //     event.preventDefault();  // Impede o reload da página

// //     let formData = new FormData(this);  // Captura os dados do formulário

// //     fetch("{% url 'verify_transaction' %}", {
// //         method: "POST",
// //         body: formData,
// //     })
// //     .then(response => response.json())
// //     .then(data => {
// //         document.getElementById("fraudResult").innerText = data.message;
// //         if (data.suspect) {
// //             document.getElementById("fraudResult").style.color = "red";
// //         } else {
// //             document.getElementById("fraudResult").style.color = "green";
// //         }
// //     })
// //     .catch(error => console.error("Erro:", error));
// // });


// // document.getElementById('fraudForm').addEventListener('submit', function(e) {
// //     e.preventDefault();
// //     alert('Formulário enviado com sucesso! (Aqui você chamaria a API ou modelo de detecção)');
// //   });
  