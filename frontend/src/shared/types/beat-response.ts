export type BeatBaseType = {
    title: string
    description: string
    picture_url: string
    file_url: string
    co_prod: string
    prod_by: string
    
    playlist_id: number
    user_id: number
    beat_pack_id: number
}

export type BeatUpdateType = {
    title: string
    description: string
    picture_url: string
    co_prod: string
    prod_by: string
}


export type BeatRelease = {
    title: string
    description: string
    co_prod: string
    prod_by: string    
}

export type BeatResponseType = BeatBaseType & {
    id: number
    is_available: boolean
    created_at: Date
}
