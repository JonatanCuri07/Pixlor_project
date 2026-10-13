export interface Product {
  id: string
  name: string
  price: number
  image: string
}

export const products: Product[] = [
  { id: 'pen', name: 'Lapicero Pixlor', price: 35, image: '/images/official/store/pen.webp' },
  { id: 'notebook', name: 'Cuaderno Creativo Pixlor', price: 70, image: '/images/official/store/notebook.webp' },
  { id: 'keychain', name: 'Llavero Pixlor', price: 80, image: '/images/official/store/keychain.webp' },
  { id: 'stickers', name: 'Stickers Holográficos Pixlor', price: 65, image: '/images/official/store/stickers.webp' },
  { id: 'cap', name: 'Gorro Pixlor', price: 120, image: '/images/official/store/cap.webp' },
  { id: 'shirt', name: 'Polo Pixlor', price: 150, image: '/images/official/store/shirt.webp' },
]
