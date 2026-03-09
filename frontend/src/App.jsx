import { useState } from "react";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import Journal from "./pages/Journal";
import CheckIn from "./pages/CheckIn";
import Dashboard from "./pages/Dashboard";

export default function App() {
  const [active, setActive] = useState("Home");
  const [journalText, setJournalText] = useState("");

  return (
    <>
      <Navbar active={active} setActive={setActive} />

      {active === "Home" && <Home />}
      {active === "Journal" && (
        <Journal
          setActive={setActive}
          setJournalText={setJournalText}
        />
      )}
      {active === "Check-in" && (
        <CheckIn
          journalText={journalText}
          setActive={setActive}
        />
      )}
      {active === "Dashboard" && <Dashboard />}
    </>
  );
}
