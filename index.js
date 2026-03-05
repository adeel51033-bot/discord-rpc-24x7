const RPC = require("discord-rpc");

const clientId = "1477986091268177982"; // Discord application ID
const rpc = new RPC.Client({ transport: "ipc" });

rpc.on("ready", () => {
  console.log("RPC started");

  rpc.setActivity({
    details: "24/7 Active",
    state: "Running on Railway",
    startTimestamp: new Date(),
    largeImageKey: "logo",
    largeImageText: "My RPC",
    instance: false
  });
});

rpc.login({ clientId }).catch(console.error);
