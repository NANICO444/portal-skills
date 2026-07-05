// kimi_chat.js
const OPENROUTER_API_KEY = process.env.OPENROUTER_API_KEY || "";

async function chatComKimi(mensagem) {
  console.log("Enviando mensagem para o Kimi...");
  
  try {
    const response = await fetch("https://openrouter.ai/api/v1/chat/completions", {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${OPENROUTER_API_KEY}`,
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        model: "moonshotai/kimi-k2.6:free",
        messages: [
          { role: "system", content: "Você é um assistente útil e amigável." },
          { role: "user", content: mensagem }
        ]
      })
    });

    if (!response.ok) {
      const errText = await response.text();
      throw new Error(`Erro na requisição: ${response.status} - ${errText}`);
    }

    const data = await response.json();
    console.log("\n================ Resposta do Kimi ================\n");
    console.log(data.choices[0].message.content);
    console.log("\n==================================================\n");

  } catch (error) {
    console.error("Falha ao comunicar com o Kimi:", error);
  }
}

// Testando a função:
chatComKimi("Olá! Qual é o seu nome e que modelo de inteligência artificial você é?");
