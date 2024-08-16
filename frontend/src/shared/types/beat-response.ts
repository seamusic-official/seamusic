import { BeatBaseType } from "./beat"


export type BeatUpdateType = {
    title: string
    description: string
    picture_url: string
    co_prod: string
    prod_by: string
}


export type BeatResponseType = BeatBaseType & {
    id: number
    is_available: boolean
    created_at: Date
}
