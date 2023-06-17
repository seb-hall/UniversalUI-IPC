pub trait ipcCodable {
    fn encodeName(&self);
    fn encodeType(&self);
    fn encodeData(&self);
}