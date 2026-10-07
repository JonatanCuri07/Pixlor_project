export interface Product {
  id: string
  name: string
  price: number
  image: string
}

export const products: Product[] = [
  { id: 'pen', name: 'Lapicero Pixlor', price: 35, image: '/images/products/pen.webp' },
  { id: 'notebook', name: 'Cuaderno Creativo Pixlor', price: 70, image: '/images/products/notebook.webp' },
  { id: 'keychain', name: 'Llavero Pixlor', price: 80, image: '/images/products/keychain.webp' },
  { id: 'stickers', name: 'Stickers Holográficos Pixlor', price: 65, image: '/images/products/stickers.webp' },
  { id: 'cap', name: 'Gorro Pixlor', price: 120, image: '/images/products/cap.webp' },
  { id: 'shirt', name: 'Polo Pixlor', price: 150, image: '/images/products/shirt.webp' },
]
