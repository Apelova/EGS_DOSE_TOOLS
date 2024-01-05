from __future__ import annotations
from typing import TYPE_CHECKING, Union, Sequence
import numpy as np

if TYPE_CHECKING:
    import numpy.typing as npt

_IntegerType = Union[int, np.integer]


class Rotation:
    def __init__(self, quat: npt.ArrayLike, normalize: bool = ..., copy: bool = ...) -> None: ...
    @property
    def single(self) -> bool: ...
    def __len__(self) -> int: ...
    @classmethod
    def from_quat(cls, quat: npt.ArrayLike) -> Rotation: ...
    @classmethod
    def from_matrix(cls, matrix: npt.ArrayLike) -> Rotation: ...
    @classmethod
    def from_rotvec(cls, rotvec: npt.ArrayLike, degrees: bool = ...) -> Rotation: ...
    @classmethod
    def from_euler(cls, seq: str, angles: float | npt.ArrayLike, degrees: bool = ...) -> Rotation: ...
    @classmethod
    def from_mrp(cls, mrp: npt.ArrayLike) -> Rotation: ...
    def as_quat(self, canonical: bool) -> np.ndarray: ...
    def as_matrix(self) -> np.ndarray: ...
    def as_rotvec(self, degrees: bool = ...) -> np.ndarray: ...
    def as_euler(self, seq: str, degrees: bool = ...) -> np.ndarray: ...
    def as_mrp(self) -> np.ndarray: ...
    @classmethod
    def concatenate(cls, rotations: Sequence[Rotation]) -> Rotation: ...
    def apply(self, vectors: npt.ArrayLike, inverse: bool = ...) -> np.ndarray: ...
    def __mul__(self, other: Rotation) -> Rotation: ...
    def inv(self) -> Rotation: ...
    def magnitude(self) -> np.ndarray | float: ...
    def mean(self, weights: npt.ArrayLike | None = ...) -> Rotation: ...
    def reduce(self, left: Rotation | None = ..., right: Rotation | None = ...,
               return_indices: bool = ...) -> Rotation | tuple[Rotation, np.ndarray, np.ndarray]: ...
    @classmethod
    def create_group(cls, group: str, axis: str = ...) -> Rotation: ...
    def __getitem__(self, indexer: int | slice | npt.ArrayLike) -> Rotation: ...
    @classmethod
    def identity(cls, num: int | None = ...) -> Rotation: ...
    @classmethod
    def random(cls, num: int | None = ...,
               random_state: _IntegerType | np.random.Generator | np.random.RandomState | None = ...) -> Rotation: ...
    @classmethod
    def align_vectors(cls, a: npt.ArrayLike, b: npt.ArrayLike,
                      weights: npt.ArrayLike | None = ...,
                      return_sensitivity: bool = ...) -> tuple[Rotation, float] | tuple[Rotation, float, np.ndarray]:...

class Slerp:
    times: np.ndarray
    timedelta: np.ndarray
    rotations: Rotation
    rotvecs: np.ndarray
    def __init__(self, times: npt.ArrayLike, rotations: Rotation) -> None: ...
    def __call__(self, times: npt.ArrayLike) -> Rotation: ...
