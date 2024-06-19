export default function DecorText({ children, font }) {
  return (
    <span className={`${font} bg-clip-text text-transparent bg-gradient-to-r from-emerald-800 to-emerald-500`}>
        {children}
    </span>
  )
}
