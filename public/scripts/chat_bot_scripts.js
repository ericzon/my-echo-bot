async function initializeChatbot() {
  const { createStore, ReactWebChat } = window.WebChat;
  const { useMemo } = window.React;

  const res = await fetch("/api/directline/token", { method: "POST" });
  const { token } = await res.json();

  const store = createStore({}, ({ dispatch }) => (next) => (action) => {
    if (
      action.payload &&
      action.payload.activity &&
      action.payload.activity.type === "event" &&
      action.payload.activity.name === "makeScreenshot" &&
      action.type === "DIRECT_LINE/INCOMING_ACTIVITY"
    ) {
      const htmlContent = document.getElementById("myForm");

      html2canvas(htmlContent).then((canvas) => {
        const base64Image = canvas.toDataURL("image/png");
        dispatch({
          type: "WEB_CHAT/SEND_EVENT",
          payload: {
            name: "screenshotRequested",
            type: "event",
            value: {
              img: base64Image,
            },
          },
        });
        return next(action);
      });
    } else {
      return next(action);
    }
  });

  const styleOptions = {
    primaryFont: "'Open Sans', sans-serif;font-size: 1em",
    backgroundColor: "#D4E1F5BF",
    bubbleBackground: "transparent",
    bubbleFromUserBackground: "transparent",
    hideUploadButton: true,
  };

  const App = () => {
    const handleButtonClick = () => {
      alert("Button clicked!");
    };

    const directLine = useMemo(
      () =>
        window.WebChat.createDirectLine({
          token,
        }),
      []
    );

    const locale = navigator.language || "en-US";

    return (
      <ReactWebChat
        directLine={directLine}
        locale={locale}
        store={store}
        styleOptions={styleOptions}
      />
    );
  };

  window.ReactDOM.render(<App />, document.getElementById("webchat"));

  document.querySelector("#webchat > *").focus();
}

(async function () {
  "use strict";

  await initializeChatbot();

  const chatIcon = document.getElementById("chatIcon");
  const webchat = document.getElementById("custom-chat-bot");

  // add a click event listener to the document
  document.addEventListener("click", (e) => {
    // check if the click event target is not the chat icon or the webchat div or any of its descendants
    if (e.target !== chatIcon && !webchat.contains(e.target)) {
      // if so, hide the webchat div
      webchat.style.display = "none";
      chatIcon.style.display = "inline-block";
    }
  });

  // add a click event listener to the chat icon image to show the webchat
  chatIcon.addEventListener("click", () => {
    webchat.style.display = "block";
    chatIcon.style.display = "none";
  });

  replaceSendIcon();
})().catch((err) => console.error(err));

function replaceSendIcon() {
  // Replace send image
  // select the SVG element
  const svgElement = document.querySelector(".webchat__send-icon");

  // create a new image element
  const imgElement = document.createElement("img");

  // set the attributes of the new image element
  imgElement.src = "img/dial.png"; // replace with the path to your new image
  imgElement.alt = "Send Icon";
  imgElement.height = 28;
  imgElement.width = 28;

  // replace the SVG element with the new image element
  svgElement.parentNode.replaceChild(imgElement, svgElement);
}

async function handleExit() {
  // Reset the token and reinitialize the chatbot
  await initializeChatbot("exit");
  document.getElementById("chatIcon").style.display = "block";
  document.getElementById("custom-chat-bot").style.display = "none";
  replaceSendIcon();
}
