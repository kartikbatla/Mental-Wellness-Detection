export default function Navbar({ active, setActive }) {
  const links = ["Home", "Journal", "Check-in", "Dashboard"];

  return (
    <nav style={styles.nav}>
      <div style={styles.logo}>🧠 MindFlow</div>

      <div style={styles.links}>
        {links.map(link => (
          <button
            key={link}
            onClick={() => setActive(link)}
            style={{
              ...styles.link,
              ...(active === link ? styles.active : {})
            }}
          >
            {link}
          </button>
        ))}
      </div>
    </nav>
  );
}

const styles = {
  nav: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    padding: "20px 48px",
    background: "#fbfaf7"
  },
  logo: {
    fontSize: "20px",
    fontWeight: 600
  },
  links: {
    display: "flex",
    gap: "16px"
  },
  link: {
    border: "none",
    background: "transparent",
    padding: "8px 16px",
    borderRadius: "20px",
    cursor: "pointer",
    fontSize: "15px",
    color: "#6b7280"
  },
  active: {
    background: "#eaf3ee",
    color: "#4f8f6f"
  }
};
